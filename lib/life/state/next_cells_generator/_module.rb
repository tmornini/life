# -*- encoding : utf-8 -*-

require 'life/state/new_row_generator/_module'

module Life
  class State
    class NextCellsGenerator
      DEFAULTS = {
        new_row_generator: NewRowGenerator
      }

      def initialize config = { }
        merged = DEFAULTS.merge config

        @new_row_generators = merged[:new_row_generator].pool
      end

      def generate args = { }
        old_cells = args[:cells]

        futures = [ ]

        old_cells.each_with_index do |old_row, y|
          futures <<
            @new_row_generators
              .future
                .generate(
                  args.merge(
                    y:       y,
                    old_row: old_row
                  )
          )
        end

        futures.collect { |future| future.value }
      end
    end
  end
end
