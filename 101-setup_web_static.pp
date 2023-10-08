class webserver {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => '<h1>Welcome to www.to-bit.tech</h1>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('webserver/default.erb'),
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
  }

  service { 'nginx':
    ensure     => 'running',
    enable     => true,
    subscribe  => [File['/etc/nginx/sites-available/default'], File['/data/web_static/current']],
  }

  firewall { '100 allow nginx http':
    proto   => 'tcp',
    port    => '80',
    action  => 'accept',
  }
}

include webserver
