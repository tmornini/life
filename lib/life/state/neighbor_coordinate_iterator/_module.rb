# -*- encoding : utf-8 -*-

module Life
  class State
    module NeighborCoordinateIterator
      def self.iterate args
        coordinates_for(args).each_with_index do |coordinates, i|
          yield coordinates.first, coordinates.last, i
        end
      end

      private

      def self.coordinates_for args
        cells = args[:cells]

        x_max = cells.first.length - 1
        y_max = cells.length - 1

        candidates_for(
          args[:x], args[:y]
        )
          .reject do |coordinates|
            invalid? coordinates, x_max, y_max
          end
      end

      def self.invalid? coordinates, x_max, y_max
        x = coordinates.first
        y = coordinates.last

        out_of_bounds?(x, x_max) || out_of_bounds?(y, y_max)
      end

      def self.out_of_bounds? i, max
        i < 0 || i > max
      end

      def self.candidates_for x, y
        [
          [ x - 1, y - 1 ], [ x, y - 1 ], [ x + 1, y - 1 ],
          [ x - 1, y     ],               [ x + 1, y     ],
          [ x - 1, y + 1 ], [ x, y + 1 ], [ x + 1, y + 1 ]
        ]
      end
    end
  end
end
