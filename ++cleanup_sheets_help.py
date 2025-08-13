# in excel (O365) you can run python
# and use lib's like pande [pd]
# 1) # dates in excel files can be a pain.  because people love to use all sorts of exotic date formats, mixed.

# =py [enter] pd.to_datetime(xl("B3")) # ctrl-enter

# switch data from columns to rows (unpivot)
# = py [enter] pd.melt(xl("b4:f18",headers = true) , di_vars=xl("B4"))  [enter]  [ctrl+alt+shift+M]

