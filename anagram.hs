-- stack --install-ghc runghc --package hashmap

import qualified Data.HashMap as M
import Data.List (sort)

main = do
  content <- readFile "/usr/share/dict/french"

  let key s = sort s
      merge l [x] = x:l
      toAssoc x = (key x, [x])

      items = map toAssoc (words content)
      groups = M.fromListWith merge items 

  print $ M.lookup (key "tortue") groups
