require_relative '../../test/test_helper'

require 'ffi'

module Mediagem
  extend FFI::Library
  ffi_lib 'c'

  lib = File.expand_path('../..', __dir__)
  ffi_lib lib + '/lib/rubyso.so'

  attach_function :myPow, [ :int, :int ], :int
end

puts Mediagem.myPow(2, 10)
