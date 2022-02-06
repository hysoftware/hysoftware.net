describe('My First Test', () => {
  beforeEach(() => {
    cy.visit('/')
  })
  it('should display SNS buttons', () => {
    const snsLinks = cy.getSNSLinks();
    snsLinks.each((el) => {
      expect(el.find('[mat-raised-button]')).is.ok;
      expect(el).is.visible;
    });
  });
  it('should display misc buttons', () => {
    const links = cy.getMiscLinks();
    links.each((el) => {
      expect(el.find('[mat-raised-button]')).is.ok;
      expect(el).is.visible;
    });
  });
  it('taget=_blank vlun check', () => {
    cy.getTargetBlankLinks().each((el) => {
      const rel = el.attr('rel');
      const values = rel.split(/\s+/);
      expect(values).contains('noopener');
      expect(values).contains('noreferrer');
    });
  });
  // it('Visits the initial project page', () => {
  //   cy.contains('Welcome')
  //   cy.contains('sandbox app is running!')
  // })
})
