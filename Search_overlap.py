
# to put a string in a set with a designated block size
def str_to_blocks(str, block_size):
    str_len = len(str)
    max_sequs = str_len - block_size + 1
    sequs = {""}
    sequs.clear()
    for i in range(max_sequs):
        sequs.add(str[i:(i + block_size)])
    return sequs


def check_overlap(str_long, str_short):

    # to initialize the variables
    block_size = 1
    longest_block = {""}
    set_l = str_to_blocks(str_long, block_size)
    set_s = str_to_blocks(str_short, block_size)
    round = 0

    # to search with a bigger block when there is any match found, until all blocks are serched in a turn.
    while round <= len(set_s):
        for the_block in set_s:
            round += 1
            if the_block in set_l:
                round = 0
                longest_block.clear()
                longest_block.add(the_block)
                block_size += 1
                set_l = str_to_blocks(str_long, block_size)
                set_s = str_to_blocks(str_short, block_size)
    
    # to search the whole set of blocks with the confrimed longest block size to get all possible results 
    set_l = str_to_blocks(str_long, block_size-1)
    set_s = str_to_blocks(str_short, block_size-1)
    for the_block in set_s:
        if the_block in set_l:
            longest_block.add(the_block)
                
    return longest_block, block_size - 1
            




str_1 = "CAGTAAACTGATCGCGCGATATCGATCTGAATTCTCTCGGCGTGAATTCGATCTGAATTCTCCGATCTGTCTGAATTCCAGACTCTCGACGTCGATCTGAATTCCAACAGTCGTAGCTCTCGGCGTCGATCGCTAAATCGCTCGATCGCTAGAGAGCTCTGAGGATATTC"
str_2 = "ATTAAACCGATCGCTAGAGACCTAGCGATCTGAATTCTCCGATCTGTCTGAAGTAGCGTCCAACAGTCGTAGCTCCTCTCGGCGATCGCTAGAGAGTCGATCGCTCGATCTGAATTCTCCGATCTGTCTGAAATGATAA"


print(check_overlap(str_1,str_2))


