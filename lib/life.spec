# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life'

Module Life do
  it 'sets VERSION' do
    subject::VERSION.must_equal '0.0.1'
  end

  it 'sets NEWLINE' do
    subject::NEWLINE.must_equal "\n"
  end

  it 'sets LIVE_CHARACTER' do
    subject::LIVE_CHARACTER.must_equal '*'
  end

  it 'sets DEAD_CHARACTER' do
    subject::DEAD_CHARACTER.must_equal ' '
  end
end
