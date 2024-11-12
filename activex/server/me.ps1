#
# Test our ActiveX component
#

$me = New-Object -ComObject ukoloff.test
$me.softspace = 5
Write-Output $me.Hello('world')
