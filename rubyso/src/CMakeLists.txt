# Add executable called "helloDemo" that is built from the source files
add_executable (rubyso.so main.cxx pow.cxx)

# public include directories we will use those link directories when building
target_link_libraries (rubyso.so LINK_PUBLIC)
