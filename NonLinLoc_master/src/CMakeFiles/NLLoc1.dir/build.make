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
include CMakeFiles/NLLoc1.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/NLLoc1.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/NLLoc1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/NLLoc1.dir/flags.make

CMakeFiles/NLLoc1.dir/NLLoc1.c.o: CMakeFiles/NLLoc1.dir/flags.make
CMakeFiles/NLLoc1.dir/NLLoc1.c.o: NLLoc1.c
CMakeFiles/NLLoc1.dir/NLLoc1.c.o: CMakeFiles/NLLoc1.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/NLLoc1.dir/NLLoc1.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/NLLoc1.dir/NLLoc1.c.o -MF CMakeFiles/NLLoc1.dir/NLLoc1.c.o.d -o CMakeFiles/NLLoc1.dir/NLLoc1.c.o -c "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/NLLoc1.c"

CMakeFiles/NLLoc1.dir/NLLoc1.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/NLLoc1.dir/NLLoc1.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/NLLoc1.c" > CMakeFiles/NLLoc1.dir/NLLoc1.c.i

CMakeFiles/NLLoc1.dir/NLLoc1.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/NLLoc1.dir/NLLoc1.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/NLLoc1.c" -o CMakeFiles/NLLoc1.dir/NLLoc1.c.s

NLLoc1: CMakeFiles/NLLoc1.dir/NLLoc1.c.o
NLLoc1: CMakeFiles/NLLoc1.dir/build.make
.PHONY : NLLoc1

# Rule to build all files generated by this target.
CMakeFiles/NLLoc1.dir/build: NLLoc1
.PHONY : CMakeFiles/NLLoc1.dir/build

CMakeFiles/NLLoc1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/NLLoc1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/NLLoc1.dir/clean

CMakeFiles/NLLoc1.dir/depend:
	cd "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/NLLoc1.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/NLLoc1.dir/depend

