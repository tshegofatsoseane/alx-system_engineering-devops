# Script to make a a manifest to fix termintion of phpp.

exec { 'fix_phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin/', '/usr/loca/bin/'],
}
