# -*- encoding : utf-8 -*-

require 'celluloid/current'
require 'celluloid/supervision'
require 'celluloid/supervision/container'
require 'celluloid/supervision/container/pool'

require 'life/state/next_cell_state_determiner/_module'

module Life
  class State
    class NewRowGenerator
      include Celluloid

      DEFAULTS = {
        next_cell_state_determiner: NextCellStateDeterminer
      }

      def initialize config = { }
        merged = DEFAULTS.merge config

        @next_cell_state_determiner = merged[:next_cell_state_determiner]
      end

      def generate args
        new_row = [ ]

        args[:old_row].each_with_index do |alive, x|
          new_row.push(
            @next_cell_state_determiner
              .determine(
                args.merge alive: alive,
                           x:     x
              )
          )
        end

        new_row
      end
    end
  end
end
