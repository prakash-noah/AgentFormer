

def get_ethucy_split(dataset):
     seqs = [
          'Rec20210315163750',
          'Rec20210315165949',
          'Rec20210322110216',
          'Rec20210323110406',
          'Rec20210401222120',
          'Rec20210514184340',
          'Rec20210517075857'
     ]
     
     if dataset == 'mlbevo':
          test = ['Rec20210401222120']

     train, val = [], []
     for seq in seqs:
          if seq in test:
               continue
          train.append(f'{seq}_train')
          val.append(f'{seq}_val')
     return train, val, test
