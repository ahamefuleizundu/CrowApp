# Makefile

CXX = g++
CXXFLAGS = -I./libs -std=c++17 -Wall
BUILD_DIR = build
SRC_DIR = src
TARGET = $(BUILD_DIR)/crow_app

# Source files
SRC_FILES = $(wildcard $(SRC_DIR)/*.cpp)

# Build the application
all: $(TARGET)

$(TARGET): $(SRC_FILES)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Clean build directory
clean:
	rm -rf $(BUILD_DIR)/*

# Format code
format:
	clang-format -i $(SRC_DIR)/*.cpp
