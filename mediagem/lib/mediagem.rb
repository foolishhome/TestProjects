require_relative 'mediagem/version'
require_relative 'config/locale'

module Mediagem
  # Your code goes here...
  class Gif
    def self.name
      return I18n.t('hello')
    end
  end
end
