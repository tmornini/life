# -*- encoding : utf-8 -*-

require 'thread'

require 'life'

require 'life/state/_class'

module Life
  module StateFileReader
    DEFAULTS = {
      file_class:  File,
      state_class: State,
      pathname:    'initial_state.txt'
    }

    ASTERISK = '*'

    MUTEX = Mutex.new

    def self.read args = { }
      merged = DEFAULTS.merge args

      cells =
        MUTEX.synchronize do
          cells_from(
            merged[:file_class]
              .open(
                merged[:pathname]
              )
          )
        end

      merged[:state_class].new cells: cells
    end

    private

    def self.cells_from file
      file.collect do |line|
        next if line.length == 1
        row_from line
      end
        .reverse
    end

    def self.row_from line
      line
        .chomp
        .each_char
        .collect do |char|
          char == LIVE_CHARACTER
        end
    end
  end
end
