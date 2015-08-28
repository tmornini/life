# -*- encoding : utf-8 -*-

require 'life'

require 'life/state/next_cells_generator/_module'

module Life
  class State
    DEFAULTS = {
      next_cells_generator: NextCellsGenerator
    }

    def initialize config
      merged = DEFAULTS.merge config

      @next_cells_generator = merged[:next_cells_generator].new

      @cells = merged[:cells]
    end

    def generate_next
      self.class.new cells: @next_cells_generator.generate(cells: @cells)
    end

    def to_s
      @cells
        .reverse
        .collect do |row|
          row.collect do |alive|
            alive ? LIVE_CHARACTER : DEAD_CHARACTER
          end
            .join
        end
        .join(NEWLINE) + NEWLINE
    end
  end
end
