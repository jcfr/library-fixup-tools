#! /usr/bin/env python

def recursively_list_file_within_directory(directory, pattern):
  """The returned list of file including the relative path to the provided directory."""
  import fnmatch
  import os

  matches = []
  for root, dirnames, filenames in os.walk(directory):
    for filename in fnmatch.filter(filenames, pattern):
      matches.append(os.path.join(root, filename))
  return matches


def get_dependencies(filepath):
  import subprocess
  p = subprocess.Popen(["otool", "-L", filepath], stdout=subprocess.PIPE)
  out, err = p.communicate()
  return out

def has_at_executable(deps):
  return "@executable" in deps
    

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option("--library-directory", dest="library_directory",
                    help="specify the directory containing the libraries to analyze")
  parser.add_option("--match-patterns", default='*.so *.dylib',
                    dest="match_patterns",
                    help="patterns used to match libraries. Example: \"*.so *.dylib\"")
  parser.add_option("--verbose",
                    dest="verbose", action="store_true",
                    help="Print verbose information")
  parser.add_option("--extra-verbose",
                    dest="extra_verbose", action="store_true",
                    help="Print extra verbose information")

  (options, args) = parser.parse_args()

  requiredArgumentErrorMessage = "argument '%s' is required !"
  if not options.library_directory:
    parser.error(requiredArgumentErrorMessage % '--library-directory')

  if options.extra_verbose: 
    options.verbose = True

  all_project_files = []
  match_patterns = options.match_patterns.split(" ")
  for match_pattern in match_patterns:
    project_files = recursively_list_file_within_directory(options.library_directory, match_pattern)
    all_project_files.extend(project_files)
    if options.verbose:
      print "Found %s files walking [%s] using [%s] pattern" % (len(project_files), options.library_directory, match_pattern)

  unfixed_libraries = []

  for filepath in all_project_files:
    deps = get_dependencies(filepath)
    fixed_up = has_at_executable(deps)
    if not fixed_up:
      unfixed_libraries.append(filepath)
    if options.extra_verbose: 
      print "Analyzing %s" % (filepath)
      if fixed_up:
        print "\t[OK]"
      else:
        print "\t[FAILED]"

  print "\nAnalysis summary"
  print "\tTotal: %s libraries" % (len(all_project_files))
  print "\tUnfixed: %s libraries" % (len(unfixed_libraries))
  
  if options.verbose: 
    print "\nList of unfixed libraries"
    for filepath in unfixed_libraries:
      print "\t%s" % filepath

