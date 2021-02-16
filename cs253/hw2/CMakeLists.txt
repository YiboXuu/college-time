cmake_minimum_required(VERSION 3.15)

    # Using -Wall is required:
    add_compile_options(-Wall)

    # These compile flags are highly recommended, but not required:
    add_compile_options(-Wextra -Wpedantic)

   

    # Create the executable hw2 from the source file hw2.cc:
    add_executable(hw2 hw2.cc)

    # Create a tar file every time:
    add_custom_target(hw2.tar ALL COMMAND tar cf hw2.tar hw2.cc CMakeLists.txt)