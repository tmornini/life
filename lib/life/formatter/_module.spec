# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'life/formatter/_module'

module Life
  Module Formatter do
    RespondsTo :format do
      ByReturning 'a nicely formatted string' do
        subject.format({ }).must_equal '{}'
      end
    end
  end
end
