# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life/state_file_reader/_module'

module Life
  Module StateFileReader do
    let(:args) do
      {
        file_class:  file_class,

        state_class: state_class,

        pathname:    pathname
      }
    end

    double :file_class

    double :state_class

    double :pathname

    double :file_instance
    double :line_1
    double :line_2
    double :chomped_line_1
    double :chomped_line_2
    double :char_1
    double :char_2

    RespondsTo :read do
      ByReturning 'an instance of State' do
        expect(file_class)
          .to receive(:open)
          .with(pathname)
          .and_return(file_instance)

        expect(file_instance)
          .to receive(:collect)
          .with(no_args)
          .and_yield(line_1)
          .and_yield(line_2)
          .and_return(
            [[true], [false]]
          )

        expect(line_1)
          .to receive(:length)
          .with(no_args)
          .and_return(2)

        expect(line_1)
          .to receive(:chomp)
          .with(no_args)
          .and_return(chomped_line_1)

        expect(chomped_line_1)
          .to receive(:each_char)
          .with(no_args)
          .and_return([char_1])

        expect(char_1)
          .to receive(:==)
          .with(subject::ASTERISK)
          .and_return(true)

        expect(line_2)
          .to receive(:length)
          .with(no_args)
          .and_return(2)

        expect(line_2)
          .to receive(:chomp)
          .with(no_args)
          .and_return(chomped_line_2)

        expect(chomped_line_2)
          .to receive(:each_char)
          .with(no_args)
          .and_return([char_2])

        expect(char_2)
          .to receive(:==)
          .with(LIVE_CHARACTER)
          .and_return(false)

        expect(state_class)
          .to receive(:new)
          .with(
            cells: [[false], [true]]
          )
          .and_return(:state_instance)

        subject.read(args).must_equal :state_instance
      end
    end
  end
end
