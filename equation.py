def solve_for_y(x_values):
    m,c=45,0.5
    print('m = {}, c = {}, then in eqn. y=mx+c,'.format(m,c))
    for x in x_values:
        y=45*x+c
        print('\nWhen x = {},\n\ty = {:.2f}'.format(x,y))

solve_for_y([1, 2.3, 5.6, 7, 78])