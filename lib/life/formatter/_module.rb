# -*- encoding : utf-8 -*-

require 'awesome_print'

module Life
  module Formatter
    def self.format thing
      thing.ai
    end

    def self.puts thing
      Kernel.puts(format thing)
    end
  end
end

AwesomePrint.defaults = { indent:    -2,
                          index:     true,
                          html:      false,
                          multiline: true,
                          plain:     false,
                          raw:       false,
                          sort_keys: false,
                          limit:     false,
                          color:     {
                            args:       :pale,
                            array:      :white,
                            bigdecimal: :blue,
                            class:      :yellow,
                            date:       :greenish,
                            falseclass: :red,
                            fixnum:     :blue,
                            float:      :blue,
                            hash:       :pale,
                            keyword:    :cyan,
                            method:     :purpleish,
                            nilclass:   :red,
                            rational:   :blue,
                            string:     :yellowish,
                            struct:     :pale,
                            symbol:     :cyanish,
                            time:       :greenish,
                            trueclass:  :green,
                            variable:   :cyanish
                          }
                        }
