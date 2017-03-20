# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'mediagem/version'

Gem::Specification.new do |spec|
  spec.name          = "mediagem"
  spec.version       = Mediagem::VERSION
  spec.authors       = ["james"]
  spec.email         = ["jamesfoolishman@gmail.com"]
  spec.description   = "xxxx"
  spec.summary       = "qqqq"
  spec.homepage      = ""
  spec.license       = "MIT"

  spec.files         = ["lib/mediagem.rb","lib/mediagem/version.rb","lib/config/locale.rb","lib/config/locales/en.yml","lib/config/locales/zh-CN.yml"] # `git ls-files`.split($/)
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.3"
  spec.add_development_dependency "rake"
end
