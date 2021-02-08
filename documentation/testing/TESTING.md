# Manually tested actions

## Navigation and header

**Item**|**Action**|**Expected result**|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
Nav links (filters)|click|Only albums matching the filter is displayed| |x
Sort select|click|Sorts current selection of albums according to chosen sorting method| |x
Logo|click|Take user to landing page/display all albums| |x
Search field|enter keyword + click|Display results| |x
My Account icon|click|Display dropdown| |x
My account links|click|Take user to correct section| |x
Cart icon|click|Display cart preview (except when viewing cart page and on small screens)| |x
Delete icon in cart preview|click|Removes album from cart| |x*


## Cart

**Item**|**Action**|**Expected result**|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
"Buy"-button (all albums- and album details view)|click|Add album to cart and display toast| |x
Delete icon in cart|click|Removes album from cart| |x
Quantity input in cart|enter number/click up/down buttons|Immediately update cart | |x
Quantity input in cart|enter invalid value (none integer 0-10)|Display helpful error message| |x