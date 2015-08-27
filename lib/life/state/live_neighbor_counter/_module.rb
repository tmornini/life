# -*- encoding : utf-8 -*-

require 'life/state/neighbor_coordinate_iterator/_module'

module Life
  class State
    module LiveNeighborCounter
      DEFAULTS = {
        neighbor_coordinate_iterator: NeighborCoordinateIterator
      }

      def self.count args
        args = DEFAULTS.merge args

        cells = args[:cells]

        live_neighbors = 0

        args[:neighbor_coordinate_iterator].iterate args do |x, y|
          live_neighbors += 1 if cells[y][x]
        end

        live_neighbors
      end

      private

      def self.cell_at cells, x, y
        cells[y][x]
      end
    end
  end
end
