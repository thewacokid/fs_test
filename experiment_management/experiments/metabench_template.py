import sys,os,time,getpass
#
# This assumes that we are sitting in the experiment_management/experiments
# directory.
#
sys.path += [ './lib', '../lib' ]
import expr_mgmt
#
# Some variables that we might use to parameterize the runs.
#
user        = getpass.getuser()
home        = os.getenv( "HOME" )
my_mpi_host = os.getenv( "MY_MPI_HOST" )
#
# Tell where the metabench program is sitting.
#
metabench_root = ( "<path-to-metabench-root" )
mpi_program = ( "%s/src/metabench" % ( metabench_root )) 
#
# The work directories of metabench.
#
work_dirs = [ "/path/to/file-system/work_dir0", "/path/to/file-system/work_dirn" ]
#
# Setup the MPI options you want to pass to the MPI launching program, for
# example, "mpirun" or "aprun".
#
# We cannot have a constant file count divided by the number of processes
# in the experiment by defining "n" here, but we do need the variable,
# mpi_options, to exist. We will then use a custom "make_commands" below.
#
mpi_options = {
#  "N"    : [ pe-count-per-node-1, ..., pe-count-pernode-n ],
#  "N"    : [ 1 ],
#  "n"   : [ 1 ],
#  "N"    : [ 2 ],
#  "n"   : [ 2 ],
#  "N"    : [ 4 ],
#  "n"   : [ 4 ],
#  "N"    : [ 8 ],
#  "n"   : [ 8 ],
  "n"   : [ 16, 32, 64, 128, 256, 512, 1024 ], 
}
#
# Metabench options
#
# In all cases, the options can be lists. The parsing program will generate
# metabench commands one at a time by picking the first element of each list.
# The next command will be generated by going to the next element of the last
# list that has multiple entries, etc.
#
# Of course, the "mpi_options" above are the first lists.
#
program_options = {
#
# The location of the Metabench dictionary.
#
  "p" : [ "%s/dictionary" % ( metabench_root ) ],
#
# The target work directory of the test.
#
  "w" : [ "%s" % ( work_dirs[0] ) ],
#  "w" : [ "%s" % ( work_dirs[1] ) ],
#  "w" : [ "%s" % ( work_dirs[0] ), "%s" % ( work_dirs[1] ) ],
#
# One process does a timed creation of the number of files specified as the
# argument.
#
#  "T" : [ 102400, 204800 ],
#
# Each process creates the number of files specified as the argument in its
# own directory. That is, this is N-N where each process of N has its own,
# unique directory. This tests the scenario where processes don't have to
# delay to get a lock on the directory from competing processes.
#
# We cannot have a constant file count divided by the number of processes
# in the experiment by defining "c" here. We will use a custom
# "make_commands" below.
#
#  "c" : [ 102400, 204800 ],
#
# Each process creates the number of files specified as the argument in a
# shared directory. That is, this is N-N where all N processes are using the
# same, shared directory. This tests the scenario where processes do have to
# delay to get a lock on the directory from competing processes.
#
# We cannot have a constant file count divided by the number of processes
# in the experiment by defining "C" here. We will use a custom
# "make_commands" below.
#
#  "C" : [ 102400, 204800 ],
#
# Runs a file stat test. There is no argument. If it's used it will stat.
# If it is not used it will not stat.
#
#  "S" : [ '' ],
#
# Runs a file update test. There is no argument. If it's used it will do
# the update test. If it is not used it will not do the update test.
#
#  "U" : [ '' ],
#
# Runs a file append test with the number of bytes specified as the argument.
#
#  "A" : [ 104856, 1048560],
#
# Runs a file delete test. There is no argument. If it's used it will
# delete. If it's not used it will not delete.
#
#  "D" : [ '' ],
#
# Tells the test program to rotate responsibility for the set of files on
# which to run a test to other processes. This makes it so that a process
# will not have the files cached. There is no argument. If it's used it will
# rotate. If it's not used it will not rotate.
#
#  "r" : [ '' ],
}

#############################################################################
# typical use of this framework won't require modification beyond this point
#############################################################################

def get_commands( expr_mgmt_options ):
  global mpi_options, mpi_program, program_options
#
# Uncomment this section when using mpi_options and "C" (or "c") from above.
#
  commands = expr_mgmt.get_commands( 
      mpi_options=mpi_options,
      mpi_program=mpi_program,
      program_options=program_options,
      expr_mgmt_options=expr_mgmt_options )
  return commands
#
# Comment this section when using mpi_options and "C" from above.
#
  #def make_commands():
  #  return expr_mgmt.get_commands(
  #      mpi_options=mpi_options,
  #      mpi_program=mpi_program,
  #      program_options=program_options,
  #      expr_mgmt_options=expr_mgmt_options )

  #commands = []

  #for exponent in range ( 0, 11 ):
  #  np = 2**exponent
  #  mpi_options['n'] = [ np ]
  #  program_options['C'] = [ 102400/np ]
  #  commands += make_commands()

  #return commands