require 'i18n'

# Where the I18n library should search for translation files
I18n.enforce_available_locales = false

I18n.config.load_path += Dir[Dir.pwd + "/lib/config/locales/*.{rb,yml}"]

# Set default locale to something other than :en
I18n.available_locales = [:"zh-CN", :en]
I18n.default_locale = :"zh-CN"
