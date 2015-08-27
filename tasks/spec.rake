# -*- encoding : utf-8 -*-

require 'rake/testtask'

namespace :spec do
  Rake::TestTask.new :unit do |task|
    task.loader     = 'file://_spec/loader'
    task.test_files = FileList['lib/**/*.spec']
  end
end
