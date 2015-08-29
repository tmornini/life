# -*- encoding : utf-8 -*-

require 'life/state/neighbor_coordinate_iterator/_module'

module Life
  class State
    module LiveNeighborCounter
      DEFAULTS = {
        neighbor_coordinate_iterator: NeighborCoordinateIterator
      }

      def self.count args
        merged = DEFAULTS.merge args

        cells = args[:cells]

        live_neighbors = 0

        merged[:neighbor_coordinate_iterator].iterate args do |x, y|
          live_neighbors += 1 if cells[y][x]
        end

        live_neighbors
      end
    end
  end
end
