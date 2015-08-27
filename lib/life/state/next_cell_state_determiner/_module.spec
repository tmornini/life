# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life/state/next_cell_state_determiner/_module'

module Life
  class State
    Module NextCellStateDeterminer do
      let(:args) do
        expect(:live_neighbor_counter)
          .to receive(:count)
          .with(args)
          .and_return(neighgors)

        {
          live_neighbor_counter: live_neighbor_counter,
          alive:                 alive
        }
      end

      double :live_neighbor_counter

      RespondsTo :determine do
        ByReturning :boolean do
          When 'center is alive' do
            let(:alive) { true }

            And 'has zero neighbors' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has one neighbor' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has two neighbors' do
              let(:neighbors) { 0 }

              ByReturning true do
                subject.determine(args).must_equal true
              end
            end

            And 'has three neighbors' do
              let(:neighbors) { 0 }

              ByReturning true do
                subject.determine(args).must_equal true
              end
            end

            And 'has four neighbors' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has five neighbors' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has six neighbors' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has seven neighbors' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has eight neighbors' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end
          end

          When 'center is dead' do
            let(:alive) { false }

            And 'has zero neighbors' do
              let(:neighbors) { 0 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has one neighbor' do
              let(:neighbors) { 1 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has two neighbors' do
              let(:neighbors) { 2 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has three neighbors' do
              let(:neighbors) { 3 }

              ByReturning true do
                subject.determine(args).must_equal true
              end
            end

            And 'has four neighbors' do
              let(:neighbors) { 4 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has five neighbors' do
              let(:neighbors) { 5 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has six neighbors' do
              let(:neighbors) { 6 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has seven neighbors' do
              let(:neighbors) { 7 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end

            And 'has eight neighbors' do
              let(:neighbors) { 8 }

              ByReturning false do
                subject.determine(args).must_equal false
              end
            end
          end
        end
      end
    end
  end
end
