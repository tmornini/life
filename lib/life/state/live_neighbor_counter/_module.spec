# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life/state/live_neighbor_counter/_module'

module Life
  class State
    Module LiveNeighborCounter do
      let(:args) do
        {
          neighbor_coordinate_iterator: neighbor_coordinate_iterator,

          cells:                        cells,
          x:                            x,
          y:                            y
        }
      end

      double :neighbor_coordinate_iterator

      let(:cells) do
        [
          [true,  false, false],
          [false, true,  false],
          [false, false, true]
        ]
      end

      let(:x) { 1 }
      let(:y) { 1 }

      RespondsTo :count do
        ByReturning 'the number of live neighbors' do
          expect(neighbor_coordinate_iterator)
            .to receive(:iterate)
            .with(args)
            .and_yield(0, 0)
            .and_yield(0, 1)
            .and_yield(0, 2)
            .and_yield(1, 0)
            .and_yield(1, 2)
            .and_yield(2, 0)
            .and_yield(2, 1)
            .and_yield(2, 2)

          subject.count(args).must_equal 2
        end
      end
    end
  end
end
