# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life/state/neighbor_coordinate_iterator/_module'

module Life
  class State
    Module NeighborCoordinateIterator do
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

      RespondsTo :iterate do
        When 'all neighbors exist' do
          ByYielding '8 coordinates' do
            results = []

            subject.iterate args do |x, y|
              results << [x, y]
            end

            results.must_equal(
              [
                [0, 0], [1, 0], [2, 0],
                [0, 1],         [2, 1],
                [0, 2], [1, 2], [2, 2]
              ]
            )
          end
        end

        When 'not all neighbors exist' do
          let(:x) { 0 }
          let(:y) { 0 }

          ByYielding 'those that do' do
            results = [ ]

            subject.iterate args do |x, y|
              results << [x, y]
            end

            results.must_equal(
              [
                [ 1, 0 ],
                [ 0, 1 ],
                [ 1, 1 ]
              ]
            )
          end
        end
      end
    end
  end
end
