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
include CMakeFiles/interface2fmm.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/interface2fmm.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/interface2fmm.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/interface2fmm.dir/flags.make

CMakeFiles/interface2fmm.dir/interface2fmm.c.o: CMakeFiles/interface2fmm.dir/flags.make
CMakeFiles/interface2fmm.dir/interface2fmm.c.o: interface2fmm.c
CMakeFiles/interface2fmm.dir/interface2fmm.c.o: CMakeFiles/interface2fmm.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/interface2fmm.dir/interface2fmm.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/interface2fmm.dir/interface2fmm.c.o -MF CMakeFiles/interface2fmm.dir/interface2fmm.c.o.d -o CMakeFiles/interface2fmm.dir/interface2fmm.c.o -c "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/interface2fmm.c"

CMakeFiles/interface2fmm.dir/interface2fmm.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/interface2fmm.dir/interface2fmm.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/interface2fmm.c" > CMakeFiles/interface2fmm.dir/interface2fmm.c.i

CMakeFiles/interface2fmm.dir/interface2fmm.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/interface2fmm.dir/interface2fmm.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/interface2fmm.c" -o CMakeFiles/interface2fmm.dir/interface2fmm.c.s

# Object files for target interface2fmm
interface2fmm_OBJECTS = \
"CMakeFiles/interface2fmm.dir/interface2fmm.c.o"

# External object files for target interface2fmm
interface2fmm_EXTERNAL_OBJECTS = \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/GridLib.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/util.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/geo.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/octtree/octtree.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/alomax_matrix/alomax_matrix.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/alomax_matrix/eigv.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/alomax_matrix/alomax_matrix_svd.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/matrix_statistics/matrix_statistics.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/vector/vector.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/ran1/ran1.c.o" \
"/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/GRID_LIB_OBJS.dir/map_project.c.o"

bin/interface2fmm.exe: CMakeFiles/interface2fmm.dir/interface2fmm.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/GridLib.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/util.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/geo.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/octtree/octtree.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/alomax_matrix/alomax_matrix.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/alomax_matrix/eigv.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/alomax_matrix/alomax_matrix_svd.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/matrix_statistics/matrix_statistics.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/vector/vector.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/ran1/ran1.c.o
bin/interface2fmm.exe: CMakeFiles/GRID_LIB_OBJS.dir/map_project.c.o
bin/interface2fmm.exe: CMakeFiles/interface2fmm.dir/build.make
bin/interface2fmm.exe: CMakeFiles/interface2fmm.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable bin/interface2fmm.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/interface2fmm.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/interface2fmm.dir/build: bin/interface2fmm.exe
.PHONY : CMakeFiles/interface2fmm.dir/build

CMakeFiles/interface2fmm.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/interface2fmm.dir/cmake_clean.cmake
.PHONY : CMakeFiles/interface2fmm.dir/clean

CMakeFiles/interface2fmm.dir/depend:
	cd "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src" "/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/CMakeFiles/interface2fmm.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/interface2fmm.dir/depend
