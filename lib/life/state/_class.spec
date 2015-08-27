# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life/state/_class'

module Life
  Class State do
    let(:args) do
      {
        next_cells_generator: next_cells_generator,
        cells:                cells
      }
    end

    double :next_cells_generator
    double :cells

    RespondsTo :new do
      ByReturning 'an instance of State' do
        subject.new(args).must_be_instance_of State
      end
    end

    Instance do
      subject { State.new args }

      let(:cells) { [ [true, false], [false, true] ] }

      RespondsTo :generate_next do
        ByReturning 'the next generation' do
          expect(next_cells_generator)
            .to receive(:generate)
            .with(cells: cells)
            .and_return(:new_cells)

          subject.generate_next.must_be_instance_of subject.class
        end
      end

      RespondsTo :to_s do
        ByReturning 'a String representation' do
          subject.to_s.must_equal " *\n" \
                                  "* \n"
        end
      end
    end
  end
end
