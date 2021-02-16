
cmake_minimum_required(VERSION 3.14)
project(cs356c++)

set(CMAKE_CXX_STANDARD 14)

set(SOURCE_FILES main.cc BlockCipher.cc BlockCipher.h StreamCipher.cc StreamCipher.h)
add_executable(hw1 ${SOURCE_FILES})