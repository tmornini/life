# -*- encoding : utf-8 -*-

require 'life/state/live_neighbor_counter/_module'

module Life
  class State
    module NextCellStateDeterminer
      DEFAULTS = {
        live_neighbor_counter: LiveNeighborCounter
      }

      def self.determine args
        merged = DEFAULTS.merge args

        live_neighbor_count =
          merged[:live_neighbor_counter].count args

        if args[:alive]
          live_neighbor_count == 2 || live_neighbor_count == 3
        else
          live_neighbor_count == 3
        end
      end
    end
  end
end
