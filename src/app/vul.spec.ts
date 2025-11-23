import { Vul } from './vul';

describe('Vul', () => {
  it('should create an instance', () => {
    const directive = new Vul();
    expect(directive).toBeTruthy();
  });
  describe('rel property check to prevent target-blank attack.', () => {
    let rel: string[];
    beforeEach(() => {
      const directive = new Vul();
      directive.ngOnInit();
      rel = directive.rel.split(/\s+/);
    });
    ['noopener', 'noreferrer', 'nofollow'].forEach(val => {
      it(`rel should contain '${val}'`, () => {
        expect(rel).toContain(val);
      });
    });
  });
});
