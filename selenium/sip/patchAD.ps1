#
# Upgrade Phone number in AD
#
$OU = 'OU=Users,OU=EKBH,OU=uxm,OU=MS,DC=omzglobal,DC=com'

$csv = Join-Path (Split-Path $PSCommandPath -Parent) data\omz2sinara.csv
$idx = @{}
foreach ($z in Import-Csv $csv -Encoding Default -Delimiter ';') {
  $idx[$z.extension] = $z
}

Get-ADUser -SearchBase $OU -Filter 'Enabled -eq $True' -Properties otherTelephone |
ForEach-Object {
  $tel = $_.otherTelephone[0]
  if (!$tel) { return }
  $next = $idx[$tel]
  if (!$next) { return }
  $tel4 = $next.'extension new'
  $_ | Set-ADUser -Replace @{otherTelephone = $tel4 }
  [PSCustomObject]@{
    name = $_.name
    old  = $tel
    new  = $tel4
  }
}
