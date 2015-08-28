# -*- encoding : utf-8 -*-

require 'life/state/next_cell_state_determiner/_module'

module Life
  class State
    module NextCellsGenerator
      DEFAULTS = {
        next_cell_state_determiner: NextCellStateDeterminer
      }

      def self.generate args = { }
        new_cells = [ ]

        args[:cells].each_with_index do |old_row, y|
          new_cells.push(
            new_row(
              args.merge(
                y: y
              ),
              old_row
            )
          )
        end

        new_cells
      end

      private

      def self.new_row args, old_row
        merged = args.merge DEFAULTS

        the_new_row = [ ]

        old_row.each_with_index do |alive, x|
          the_new_row.push(
            merged[:next_cell_state_determiner]
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
