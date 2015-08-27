# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life/state/next_cells_generator/_module'

module Life
  class State
    Module NextCellsGenerator do
      RespondsTo :generate do
        ByReturning 'new cells' do
        end
      end
    end
  end
end
