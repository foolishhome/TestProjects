require "mediagem/version"
require 'config/locale'

module Mediagem
  # Your code goes here...
  class Gif
    def self.name
      return I18n.t('hello')
    end
  end
end
