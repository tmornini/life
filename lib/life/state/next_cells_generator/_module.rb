# -*- encoding : utf-8 -*-

require 'life/state/next_cell_state_determiner/_module'

module Life
  class State
    module NextCellsGenerator
      DEFAULTS = {
        next_cell_state_determiner: NextCellStateDeterminer
      }

      def self.generate args = { }
        new_cells args
      end

      private

      def self.new_cells args
        args = DEFAULTS.merge args

        old_cells = args[:cells]

        the_new_cells = [ ]

        old_cells.each_with_index do |old_row, y|
          the_new_cells.push(
            new_row(
              args.merge(
                y: y
              ),
              old_row
            )
          )
        end

        the_new_cells
      end

      def self.new_row args, old_row
        the_new_row = [ ]

        old_row.each_with_index do |alive, x|
          the_new_row.push(
            args[:next_cell_state_determiner]
              .determine(
                args.merge x:     x,
                           alive: alive
              )
          )
        end

        the_new_row
      end
    end
  end
end
