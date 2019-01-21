import { AppPage } from './app.po';

describe('workspace-project App', () => {
  let page: AppPage;

  beforeEach(() => {
    page = new AppPage();
    page.navigateTo();
  });

  it('should display SNS buttons', () => {
    const snsLinks = page.getSNSLinks();
    snsLinks.each(el => {
      expect(el.getAttribute('mat-raised-button'))
        .toBeTruthy('Need Material Raised Button');
      expect(el.isDisplayed())
        .toBeTruthy('Need to be displayed');
    });
  });
  it('should display misc buttons', () => {
    const links = page.getMiscLinks();
    links.each(el => {
      expect(el.getAttribute('mat-raised-button'))
        .toBeTruthy('Need Material Raised Button');
      expect(el.isDisplayed())
        .toBeTruthy('Need to be displayed');
    });
  });
});
