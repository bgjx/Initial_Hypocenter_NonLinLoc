# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake.exe

# The command to remove a file.
RM = /usr/bin/cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src"

# Include any dependencies generated for this target.
include CMakeFiles/calc_crust_corr.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/calc_crust_corr.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/calc_crust_corr.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/calc_crust_corr.dir/flags.make

CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o: CMakeFiles/calc_crust_corr.dir/flags.make
CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o: calc_crust_corr.c
CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o: CMakeFiles/calc_crust_corr.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o -MF CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o.d -o CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o -c "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/calc_crust_corr.c"

CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/calc_crust_corr.c" > CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.i

CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/calc_crust_corr.c" -o CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.s

calc_crust_corr: CMakeFiles/calc_crust_corr.dir/calc_crust_corr.c.o
calc_crust_corr: CMakeFiles/calc_crust_corr.dir/build.make
.PHONY : calc_crust_corr

# Rule to build all files generated by this target.
CMakeFiles/calc_crust_corr.dir/build: calc_crust_corr
.PHONY : CMakeFiles/calc_crust_corr.dir/build

CMakeFiles/calc_crust_corr.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/calc_crust_corr.dir/cmake_clean.cmake
.PHONY : CMakeFiles/calc_crust_corr.dir/clean

CMakeFiles/calc_crust_corr.dir/depend:
	cd "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/calc_crust_corr.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/calc_crust_corr.dir/depend

