# -*- encoding : utf-8 -*-

require 'life'

require 'life/state/_class'

module Life
  module StateFileReader
    DEFAULTS = {
      state_class: State,
      file_class:  File,
      pathname:    'initial_state.txt'
    }

    ASTERISK = '*'

    def self.read args = { }
      args = DEFAULTS.merge args

      cells =
        cells_from(
          args[:file_class]
            .open(
              args[:pathname]
            )
        )

      args[:state_class].new cells: cells
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
