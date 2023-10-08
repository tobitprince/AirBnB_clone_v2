# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Allow incoming HTTP connections
firewall { '100 allow http':
  action => 'accept',
  dport  => '80',
  proto  => 'tcp',
}

# Create directories
file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Add test string
file { '/data/web_static/releases/test/index.html':
  content => '<h1>Welcome to www.to-bit.tech</h1>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Prevent overwrite
if File['/data/web_static/current'] {
  file { '/data/web_static/current':
    ensure => 'absent',
    force  => true,
  }
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
