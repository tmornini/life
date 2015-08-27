# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life'

Module Life do
  it 'sets VERSION' do
    subject::VERSION.must_equal '0.0.1'
  end
end
