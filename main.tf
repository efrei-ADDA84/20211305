# Provider Azure
provider "azurerm" {
  features {}
}

# Variables

variable "location" {
  default = "francecentral"
}

variable "vm_name" {
  default = "devops-20211305"
}   

resource "azurerm_public_ip" "public_ip" {
  name                = "20211305-public_ip"
  location            = var.location
  resource_group_name = "ADDA84-CTP"
  allocation_method   = "Dynamic"
}

resource "azurerm_network_interface" "interface" {
  name                = "20211305-interface"
  location            = var.location
  resource_group_name = "ADDA84-CTP"

  ip_configuration {
    name                          = "20211305-ip_conf"
    subnet_id                     = "/subscriptions/765266c6-9a23-4638-af32-dd1e32613047/resourceGroups/ADDA84-CTP/providers/Microsoft.Network/virtualNetworks/network-tp4/subnets/internal"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.public_ip.id
  }

}

resource "azurerm_linux_virtual_machine" "vm" {
  name                = var.vm_name
  location            = var.location
  resource_group_name = "ADDA84-CTP"
  network_interface_ids = [azurerm_network_interface.interface.id]
  size                = "Standard_D2s_v3"

  os_disk {
    name              = "20211305-osdisk"
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }

  admin_username = "devops"
  

  admin_ssh_key {
    username       = "devops"
    public_key     = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCswRQlE/HBsD7ND7AV5nJZ8xL3NM1JUWrjoLLF459puauZSdCA7JQqa2oUacRu/gIgtxLz9XiY3CO2I0cZL0JZQ6tnLt/zfTz2z5o8NkUki2H+ZkC7/GWyXw5g873aBtor60dJd3obEkEXOKkYahUjJ5ccCbxMmwPiKVNyxPMGH4Z06jFfeZ0Mzd70rsHnHftocbw4scnLnzWhv/8QWbHTBvMudqGCPnrMcWzQNYOOFgmNSahEjo50CISy0imHG/VXDdZ8V/33srZGZ2Nggv72cGU/xPNtB++E6IrsgwD4UYaSE7IbVNNqdB40RUszDaapVDaaWh56/omzIzb+MZP/Us5SC8/mA75HLggi8e6Mv04nm3Y68EKOLAUdCGaSZX80ilgeTxCWU7TkIgrcoNiZjvntnud0SFJrM8+kcK4h0tztOzPGMPEyZS6d9i3j0tHi8FVLENFRwR3ug/lt/DUFeLec1TZ1wNSjPYYrSlMzm3MHxPXELAyXly9uBxQEDCk+PgAmNIO9ZiEM14sRQziCB4GLmO0ZHeX1azfzsMUWs7DBdAyFQnasoXY+4C7b4dRQk7Ee2sbWDXa2H4qImAmnOIthkwrzVpU3Wn0+0OkRepSGN3+yBIH8R72nkua0VKjwgKocVB5fKodoAL6oM4Da7+GVU33veNWeJ6Z1m+5cfw== tang.stephane.94@gmail.com"
  }

  
}