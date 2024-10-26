# CMakeLists.txt
cmake_minimum_required(VERSION 3.10)
project(CrowApp)

set(CMAKE_CXX_STANDARD 17)
set(CROW_LIB_DIR ${PROJECT_SOURCE_DIR}/Libs)

add_executable(CrowApp src/main.cpp)
target_include_directories(CrowApp PRIVATE ${PROJECT_SOURCE_DIR}/Libs)
