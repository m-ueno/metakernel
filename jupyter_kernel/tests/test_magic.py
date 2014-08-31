from jupyter_kernel import Magic, option


class Dummy(Magic):

        @option(
        '-s', '--size', action='store',
        help='Pixel size of plots, "width,height"'
         )
        def line_dummy(self, foo, size=None):
            """%dummy [options] foo - Perform dummy operation on foo"""
            self.foo = foo
            self.size = size

        def cell_spam(self):
            """%spam - Cook some spam"""
            pass

        def line_eggs(self, style):
            """%eggs STYLE - cook some eggs in the given style"""
            pass


def test_get_magics():
    d = Dummy(None)
    line = d.get_magics('line')
    cell = d.get_magics('cell')

    assert 'dummy' in line
    assert 'spam' in cell
    assert 'eggs' in line


def test_get_help():
    d = Dummy(None)

    dummy_help = d.get_help('line', 'dummy')
    assert dummy_help == d.line_dummy.__doc__

    spam_help = d.get_help('cell', 'spam')
    assert spam_help == d.cell_spam.__doc__


def test_option():
    d = Dummy(None)
    assert 'Options:' in d.line_dummy.__doc__
    assert '--size' in d.line_dummy.__doc__

    ret = d.call_magic('line', 'dummy', '', 'hey -s400,200')
    assert ret == d
    assert d.foo == 'hey'
    assert d.size == '400,200'
